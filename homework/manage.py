import logging

import uvicorn

from app.container import APP_CONTAINER
from app.maker import get_app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    app = get_app()
    app_settings = APP_CONTAINER.app_settings()

    uvicorn.run(app, host=app_settings.host, port=app_settings.port)

    logger.info(f"Starting server on {app_settings.host}:{app_settings.port}")
