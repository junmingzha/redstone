general_list = [

            { 'nodeinfo_list': {
                        'hostname': 'k8s-node-4',
                        'hostip': '192.168.151.17',
                        'domain': 'allbright.local',
                        },
            },
            { 'cert_files': {
                        'cacert': '/project/k8s-ui/assets/certs/ca.pem',
                        'cakey': '/project/k8s-ui/assets/certs/ca-key.pem',
                        'registry_ca': '/project/k8s-ui/assets/certs/ca.crt',
                        'ssl_conf': '/project/k8s-ui/nodes/archive/worker-openssl.conf',

                        },
            },
            {'local_path_list': {
                'tpl_path': '/project/k8s-ui/assets/templates',
                'conf_archive_path': '/project/k8s-ui/nodes/archive',
                'cert_archive_path': '/project/k8s-ui/assets/certs',
                        },
            }
        ]

deploy_list = [

    { 'generate_list': [

                {'remote_dir': '/etc/kubernetes/ssl',
                                'files': [ 'k8s-node-4' + '.pem', 'k8s-node-4' + '-key.pem' ] },
                {'remote_dir': '/etc/kubernetes/tokens',
                                'files': ['system:' + 'k8s-node-4' + '.token']},
                ]
    },
    { 'render_file_list': [
                { 'remote_dir': '/etc/kubernetes', 'files': [ 'kubelet.env', 'node-kubeconfig.yaml' ] },
                { 'remote_dir': '/etc/kubernetes/manifests', 'files': [ 'flannel-pod.manifest','kube-proxy.manifest' ] },

                { 'remote_dir': '/etc/kubernetes/ssl', 'files': [ 'worker-openssl.conf' ]},
                ]
    },
    { 'netcopy_list': [
                    { 'remote_dir': '/etc/kubernetes/ssl', 'files': [ 'ca.pem' ] },
                    { 'remote_dir': '/etc/docker/certs.d/registry.allbright.local:5000', 'files': ['ca.crt'] },
                    { 'remote_dir': '/etc/systemd/system', 'files': [ 'kubelet.service' ]},
                    { 'remote_dir': '/opt/bin', 'files': [ 'kubelet', 'kube-gen-token.sh', 'mk-docker-opts.sh', 'deploy-script.sh' ] },
                    { 'remote_dir': '/etc/flannel/certs', 'files': ['ca_cert.crt', 'cert.crt', 'key.pem' ]}

                    ],
    },

]