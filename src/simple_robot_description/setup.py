from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'simple_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         # Include all launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        # Include model and simulation files
        (os.path.join('share', package_name, 'models'), glob('models/*/*.xacro')),
        (os.path.join('share', package_name, 'models'), glob('models/*/*.sdf')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='leo',
    maintainer_email='amanyamy@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
         'console_scripts': [
                'joint_commander = simple_robot_description.joint_commander:main',
        ],
    },
)
