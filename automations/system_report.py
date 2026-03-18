from datetime import datetime
import platform

from utils.logger import log


def generate_report():
    system = platform.system()
    node = platform.node()

    report = {
        "system": system,
        "machine": platform.machine(),
        "processor": platform.processor() or "Unknown",
        "python_version": platform.python_version(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }

    log(f"System report generated for {node}")
    return report
