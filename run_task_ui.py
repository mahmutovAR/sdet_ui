from os import system as os_system
from os.path import join as os_path_join
from webbrowser import open as open_report


def main():
    # run tests
    os_system('pytest tests/ -n 3 --alluredir=allure-results --clean-alluredir')

    # add environment.properties file
    env_data = ['os_platform = Linux\n',
                'os_release = 6.8.0-40-generic\n',
                'os_version = Ubuntu 24.04 LTS\n',
                'python_version = Python 3.10.14']
    with open(os_path_join('allure-results', 'environment.properties'), 'w') as env_file:
        for line in env_data:
            env_file.write(line)

    # generate report
    os_system('allure generate allure-report --clean --single-file allure-results')

    open_report(os_path_join('allure-report', 'index.html'))


if __name__ == '__main__':
    main()
