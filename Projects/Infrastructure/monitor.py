import json
import os
import time
from datetime import datetime

class TrainingMonitor:
    def __init__(self, log_dir="logs", run_name="run_001"):
        os.makedirs(log_dir, exist_ok=True)
        self.log_path = os.path.join(log_dir, f"{run_name}_summary.json")
        
        self.history = []
        self.alerts = []
        self.start_time = time.time()
        
        # Reset file for fresh run
        with open(self.log_path, "w") as f:
            pass
    def log_epoch(self, epoch, loss, accuracy, lr=0.1, duration_sec=None):
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "epoch": epoch,
            "loss": float(loss),
            "accuracy": float(accuracy),
            "lr": float(lr),
            "duration_sec": None if duration_sec is None else float(duration_sec)
        }

        self.history.append(entry)

        with open(self.log_path, "a") as f:
            f.write(json.dumps(entry) + "\n")

        self._check_alerts()

    def _check_alerts(self):
        n = len(self.history)
        latest = self.history[-1]

        # Alert 1: NaN loss
        if latest["loss"] != latest["loss"]:  # NaN check
            self.alerts.append({
                "type": "nan_loss",
                "message": f"Loss became NaN at epoch {latest['epoch']}"
            })

        # Alert 2: Loss increasing 3 epochs in a row
        if n >= 4:
            l1 = self.history[-4]["loss"]
            l2 = self.history[-3]["loss"]
            l3 = self.history[-2]["loss"]
            l4 = self.history[-1]["loss"]
            if l1 < l2 < l3 < l4:
                self.alerts.append({
                    "type": "loss_increasing",
                    "message": f"Loss increased for 3 consecutive epochs ending at epoch {latest['epoch']}"
                })

        # Alert 3: Accuracy too low after 10 epochs
        if n >= 10 and latest["accuracy"] < 0.60:
            self.alerts.append({
                "type": "low_accuracy",
                "message": f"Accuracy remains low ({latest['accuracy']:.3f}) at epoch {latest['epoch']}"
            })

    def finalize(self):
        total_runtime = time.time() - self.start_time

        best_loss = min(h["loss"] for h in self.history) if self.history else None
        best_acc = max(h["accuracy"] for h in self.history) if self.history else None

        summary = {
            "epochs_ran": len(self.history),
            "best_loss": best_loss,
            "best_accuracy": best_acc,
            "num_alerts": len(self.alerts),
            "alerts": self.alerts,
            "total_runtime_sec": total_runtime,
            "log_file": self.log_path
        }

        with open(self.summary_path, "w") as f:
            json.dump(summary, f, indent=2)

        return summary