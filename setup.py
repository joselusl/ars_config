from setuptools import find_packages, setup
import os
from glob import glob
import fnmatch


package_name = 'ars_config'



def get_data_files_type(package_name, file_dir, file_type='*'):
    paths = []
    for (path, directories, filenames) in os.walk(file_dir):
        for filename in filenames:
            if fnmatch.fnmatch(filename, file_type):
                paths.append(os.path.join(path, filename))
                #print(os.path.join(path, filename))
    return paths

def get_data_files_type_tuple(package_name, file_dir, file_type='*'):
    paths = []
    for (path, directories, filenames) in os.walk(file_dir):
        for filename in filenames:
            if fnmatch.fnmatch(filename, file_type):
                paths.append((os.path.join('share', package_name, file_dir), os.path.join(path, filename)))
                #print(os.path.join(path, filename))
    return paths




#print((os.path.join('share', package_name, 'config'), get_data_files_type(package_name, 'config', '*.rviz')))


#print(get_data_files_type('/home/joselusl/workspace/src/ars_project/config', 'config', '*.yaml'))

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #(os.path.join('share', package_name, 'config'), (os.path.join('config', '*.[tra][ttp][cal]*'))),
        (os.path.join('share', package_name, 'config'), get_data_files_type(package_name, 'config/', '*.rviz')),
        #get_data_files_type_tuple(package_name, 'config', '*.rviz'),
        #(os.path.join('share', package_name, 'config'), glob('config/**/*.rviz', recursive=True)),
        #(os.path.join('share', package_name, 'config'), glob('config/*.rviz', recursive=True))
        #(os.path.join('share', package_name, 'config'), (os.path.join('config', '*.yaml'))),
     ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joselusl',
    maintainer_email='joseluis.sanlop@gmail.com',
    description='TODO: Package description',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
