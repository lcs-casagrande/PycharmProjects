import speedtest
test = speedtest.Speedtes()
down = test.dowload()
upload = test.upload()
print(f'Dowload speed: {down}')
print(f' Upload speed: {upload}')

