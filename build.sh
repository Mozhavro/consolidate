pyinstaller -F --name="consolidate" \
            --paths="src/" \
            --log-level=DEBUG \
            --add-data="res:res" \
            ./src/main.py 