pipeline {
    agent any
    triggers {
        pollSCM '*/5 * * * *'
    }
    stages {
        stage('Trigger Ansible Deployment') {
            steps {
                sh script:'''
          #!/bin/bash
          echo "This is start $(pwd)"
          cd /var/www/
          echo "This is $(pwd)"
          cat deploy.yml
          sudo ansible-playbook deploy.yml
          
        '''
            }
        }
    }
}
