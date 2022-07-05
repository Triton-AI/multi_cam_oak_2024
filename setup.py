from setuptools import setup

package_name = 'multi_cam'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chengjing',
    maintainer_email='cyuan@ucsd.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cams = multi_cam.multi_cam_node:main',
            'subs = multi_cam.cam_subscriber_node:main'
        ],
    },
)
