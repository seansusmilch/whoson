import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
import confuse
from pathlib import Path
import sys


folder = Path(__file__).parent.absolute()
conf = confuse.Configuration('WhosOn', __name__)
possible_config = [
    f'{folder}/config.yml',
    f'{folder}/config.yaml',
    f'/config/config.yml',
    f'/config/config.yaml'
]
conf_file = Path( possible_config.pop(0) )
while not conf_file.exists():
    if not possible_config:
        print('Config file not found!!!')
        sys.exit(1)
    conf_file = Path( possible_config.pop(0) )
print(f'Using config file at {conf_file}')
conf.set_file(conf_file)


if __name__ == '__main__':
    from web import app
    asyncio.run(serve(app, Config.from_mapping(conf['hypercorn'].get())))