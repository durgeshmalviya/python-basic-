import speedtest

st = speedtest.Speedtest()

download = st.download()
upload = st.upload()


print("Your Download speed is", download)
print("Your Download speed is", upload)
