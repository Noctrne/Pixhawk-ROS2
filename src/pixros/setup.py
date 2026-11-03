from setuptools import find_packages, setup

package_name = 'pixros'

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
    maintainer='dhipta',
    maintainer_email='dhipta@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'datacenter_node = pixros.datacenter_node:main',
            'att_node = pixros.att_node:main',
            'baro_node = pixros.baro_node:main'
        ],
    },
)
