from app import create_app
from app.cleaners import scheduler


app=create_app()
if __name__ == '__main__':
    if not scheduler.running:
        scheduler.start()
        print("Scheduler started. Running Flask app...")
    else:
        print("Scheduler is already running.")
    app.run(debug=True)