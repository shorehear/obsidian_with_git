import os
import datetime
import psutil
import time
import subprocess

obsidian_path = '/путь/до/вашей/директории'

def is_obsidian_running():
    current_date = datetime.datetime.now().isoformat()
    with open(obsidian_path + '/logger.txt', 'a') as log:
        for process in psutil.process_iter(['name']):
            if 'obsidian' in process.info['name'].lower():
                log.write(f'{current_date}, obsidian running\n')
                log.flush()
                return True
        log.write(f'{current_date}, obsidian not running\n')
        log.flush()
        return False

def git_push():
     with open(obsidian_path + '/logger.txt', 'a') as log:
        try:
            os.chdir(obsidian_path)

            subprocess.run(['git', 'add', '.'], check = True)

            commit_message = f'autocommit {datetime.datetime.today().isoformat()}'

            subprocess.run(['git', 'commit', '-m', commit_message], check=True)
            subprocess.run(['git', 'push'], check=True)

            log.write(f'{datetime.datetime.today().isoformat()}, changes have been push\n')
            log.flush()

        except subprocess.CalledProcessError as e:
            log.write(f'{datetime.datetime.today().isoformat()}, error with executing comm: {e}\n')
            log.flush()
        except Exception as e:
            log.write(f'{datetime.datetime.today().isoformat()}, summary error: {e}\n')
            log.flush()

if __name__ == '__main__':
    while is_obsidian_running():
        git_push()
        time.sleep(1800)
