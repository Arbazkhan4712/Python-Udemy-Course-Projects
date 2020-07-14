import speedtest
s = speedtest.Speedtest()
s.get_best_server()
s.download()