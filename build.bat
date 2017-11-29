pyinstaller -F --name="consolidate.exe" ^
            --noupx --paths="src/" ^
            --log-level=DEBUG ^
            --add-data="res;res" ^
            ./src/main.py 