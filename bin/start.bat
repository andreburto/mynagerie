@echo off

if %CD:~-3%==bin cd ..

docker run -it --rm --env-file "%CD%\.env" --mount type=bind,source="%CD%\src",target=/app/src --mount type=bind,source="%CD%\data",target=/app/data -p 8000:8000 mynagerie %1
