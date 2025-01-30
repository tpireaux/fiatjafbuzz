from .celery_app import celery_app
import logging

logger = logging.getLogger(__name__)


@celery_app.task
def run_bot():
    from .main import main

    try:
        main()
        logging.info("run_bot executed successfully.")
    except Exception as e:
        logging.error(f"run_bot failed: {e}")
        raise
