((nil . ((eval .
               (progn (defun zelpy-run ()
                        "Compile and run ZelPy server and client"
                        (interactive)

                        ;; Move to reserved workspace
                        (exwm-workspace-switch-create 9)

                        ;; Kill game if it is already running
                        (delete-other-windows)
                        (if (get-buffer "ZelPy")
                            (kill-buffer "ZelPy"))

                        (defun start-server ()
                          "Start game server"
                          (let ((default-directory "~/src/ZelPy/server/"))
                            (start-process "my-process" "ZelPy" "~/src/ZelPy/server/bin/python3.6" "server.py" "0.0.0.0" "5005")))

                        (defun start-client ()
                          "Start game client"
                          (let ((default-directory "~/src/ZelPy/client/"))
                            (start-process "my-process" "ZelPy" "~/src/ZelPy/client/bin/python3.6" "client.py" "enzuru" "0.0.0.0" "0" "snes")))

                        (defun process-launched (process status)
                          "Print process status"
                          (message (concat process " status " status)))

                        (defun setup-workspace ()
                          "Setup tiling on my workspace using exwm"
                          (switch-to-buffer "ZelPy")
                          (split-window-vertically)
                          (other-window 1)
                          (split-window-horizontally)
                          (switch-to-buffer-other-frame (get-buffer "server.py<2>"))
                          (exwm-floating-toggle-floating)
                          (other-window 1)
                          (switch-to-buffer-other-frame (get-buffer "client.py<2>"))
                          (exwm-floating-toggle-floating)
                          (switch-to-buffer-other-window "ZelPy"))

                        ;; Start processes monitored by sentinels, and after a 5 second delay setup the workspace
                        (let ((process (start-server)))
                          (when server-process
                            (progn
                              (set-process-sentinel server-process 'process-launched)
                              (let ((client-process (start-client)))
                                (when client-process
                                  (progn
                                    (set-process-sentinel client-process 'process-launched)
                                    (run-at-time "10 sec" nil 'setup-workspace))))))))

                      (local-set-key (kbd "C-x c") 'zelpy-run))))))
