pyinstaller -F --name="consolidate.exe" ^
            --paths="src/" ^
            --log-level=DEBUG ^
            --add-data="res;res" ^
            ./src/main.py 