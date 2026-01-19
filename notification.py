import time

from plyer import notification

if __name__ == "__main__":
    # Display a notification
    while True:
        notification.notify(
            title="ALERT",
            message="Take a Break. It has been an Hour.",
            timeout=10  # Duration in seconds
    )

    # Wait for a while to ensure the notification is displayed
        time.sleep(3600)