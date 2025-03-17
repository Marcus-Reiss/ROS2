from setuptools import find_packages, setup

package_name = 'flamingo_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros_ws',
    maintainer_email='ros_ws@todo.todo',
    description='ROS2 package for controlling Flamingo robot',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'flamingo_controller = flamingo_robot.flamingo_controller:main'
        ],
    },
)
