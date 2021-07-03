$files = @(
    './requirements.txt'
    './bot.py'
    './Dockerfile'
    './prod.py'
    './web.py'
    './.dockerignore'
)


tar -czvf whos-on.tar.gz $files