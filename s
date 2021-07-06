● supervisor.service - Supervisor process control system for UNIX
     Loaded: loaded (/lib/systemd/system/supervisor.service; enabled; vendor preset: enabled)
     Active: inactive (dead) since Mon 2021-07-05 12:56:02 PDT; 5s ago
       Docs: http://supervisord.org
    Process: 19944 ExecStart=/usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf (code=killed, signal=TERM)
    Process: 20957 ExecStop=/usr/bin/supervisorctl $OPTIONS shutdown (code=exited, status=0/SUCCESS)
   Main PID: 19944 (code=killed, signal=TERM)

Jul 05 12:41:42 ubuntu systemd[1]: Started Supervisor process control system for UNIX.
Jul 05 12:41:42 ubuntu supervisord[19944]: 2021-07-05 12:41:42,367 CRIT Supervisor is running as root.  Privileges were not dropped because no user is specified in the config file.  If you intend to run as root, you can set user=root in the config file to avoid this message.
Jul 05 12:41:42 ubuntu supervisord[19944]: 2021-07-05 12:41:42,368 WARN No file matches via include "/etc/supervisor/conf.d/*.conf"
Jul 05 12:41:42 ubuntu supervisord[19944]: 2021-07-05 12:41:42,377 INFO RPC interface 'supervisor' initialized
Jul 05 12:41:42 ubuntu supervisord[19944]: 2021-07-05 12:41:42,377 CRIT Server 'unix_http_server' running without any HTTP authentication checking
Jul 05 12:41:42 ubuntu supervisord[19944]: 2021-07-05 12:41:42,377 INFO supervisord started with pid 19944
Jul 05 12:56:02 ubuntu systemd[1]: Stopping Supervisor process control system for UNIX...
Jul 05 12:56:02 ubuntu supervisorctl[20957]: Shut down
Jul 05 12:56:02 ubuntu systemd[1]: supervisor.service: Succeeded.
Jul 05 12:56:02 ubuntu systemd[1]: Stopped Supervisor process control system for UNIX.
