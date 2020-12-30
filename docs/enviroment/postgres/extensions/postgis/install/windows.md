* Установите `Postgis` с помощью `Stack Builder`. Postgis находится в разделе `Spatial Extensions`
* Скачайте 64-битный [установщик OSGeo4W](https://trac.osgeo.org/osgeo4w/)
* Установите `OSGeo4W` выбрав установку Веб-ГИС. В списке "Выбрать пакеты" выберите `GDAL`
* Запустите консоль от имени администратора и выполните следующие команды:
```
set OSGEO4W_ROOT=C:\OSGeo4W64
set GDAL_DATA=%OSGEO4W_ROOT%\share\gdal
set PROJ_LIB=%OSGEO4W_ROOT%\share\proj
set PATH=%PATH%;%OSGEO4W_ROOT%\bin
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /t REG_EXPAND_SZ /f /d "%PATH%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v GDAL_DATA /t REG_EXPAND_SZ /f /d "%GDAL_DATA%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PROJ_LIB /t REG_EXPAND_SZ /f /d "%PROJ_LIB%"
```