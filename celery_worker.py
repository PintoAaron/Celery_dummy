from celery import Celery
from celery.schedules import crontab
from db import get_db
from models import User
from sqlalchemy.orm import Session

celery_app = Celery(
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

celery_app.conf.beat_schedule = {
    "update-every-midday": {
        "task": "celery_worker.set_active",
        "schedule": crontab(hour=12,minute=00),
    }
}


@celery_app.task()
def set_active():
    try:
        print("UPDATING IS ACTIVE FOR USERS")

        db: Session = next(get_db())
        users = db.query(User).all()

        for user in users:
            user.is_active = True
            print("is_active field updated")

        db.commit()
        print("DONE!!!")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()
    


