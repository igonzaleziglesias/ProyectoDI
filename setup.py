import setuptools

descripcion_longa = open('Readme.txt').read()

setuptools.setup(
    name="Proyecto Desarrollo Interfaces",
    version="0.0.1",
    author="igonzaleziglesias",
    author_email="igonzaleziglesias@danielcastelao.org",
    url="https://www.danielcastelao.org",
    license="GLP",
    platforms="Unix",
    clasifiers=["Development Status :: 3 - Alpha",
                "Environment :: Console",
                "Topic :: Software Development :: Libraries",
                "License :: OSI Aproved :: GNU General Public License",
                "Programming Language :: Python :: 3.6.9",
                "Operating System :: Linux Ubuntu"
                ],
    description="Base de datos",
    long_description=descripcion_longa,
    keywords='ProyectoDesarrolloInterfaces',
    packages=['Aplicacion','Aplicacion/BaseDatos','Aplicacion/GestionClientes','Aplicacion/GestionProductos','Aplicacion/Imagenes'
              ,'Aplicacion/Pedidos'],
    scripts=["Aplicacion/launcherApp"],
)
