import psutil

cpu_t_p = psutil.cpu_times_percent(interval=1, percpu=False)._asdict()
disk_usage = psutil.disk_usage('/')._asdict()
#tmp_dict = tmp._asdict()
cpu_t_p.update(disk_usage)
#cpu_idle = tmp.idle

dict_test = {'user': 'tommaso', 'psw': 'dcml'}

#print(tmp)
