from app import app as application

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    from hypercorn.asyncio import serve
    from hypercorn.config import Config
    import asyncio

    config = Config()
    config.bind = [f'0.0.0.0:{port}']

    asyncio.run(serve(application, config))

