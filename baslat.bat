@echo off
setlocal enabledelayedexpansion
title KPSS Quest - Genel Yetenek & Genel Kultur
echo ===================================================
echo           KPSS Quest Baslatiliyor
echo ===================================================
echo.

:: Calisma dizinini bat dosyasinin bulundugu klasore ayarla
cd /d "%~dp0"

:: build\web klasoru var mi kontrol et, yoksa derle
if not exist "build\web\index.html" (
    echo [1/3] Web derlemesi bulunamadi, derleme baslatiliyor...
    echo Paketler yukleniyor (flutter pub get)...
    call flutter pub get
    if errorlevel 1 (
        echo [HATA] flutter pub get basarisiz oldu! Flutter SDK yuklu mu?
        pause
        exit /b 1
    )
    
    echo Web surumu derleniyor (flutter build web)...
    call flutter build web
    if errorlevel 1 (
        echo [HATA] flutter build web basarisiz oldu!
        pause
        exit /b 1
    )
)

echo [2/3] Yerel web sunucusu baslatiliyor (Port: 8080)...
start "KPSS Quest Web Sunucusu" /min python -m http.server 8080 --directory build\web

echo [3/3] Tarayici aciliyor...
timeout /t 2 >nul
start http://localhost:8080

echo.
echo ===================================================
echo   Uygulama tarayicinizda acildi!
echo   Adres: http://localhost:8080
echo ===================================================
echo.
echo Sunucuyu kapatmak istediginizde bu pencereyi kapatabilirsiniz.
pause
