from distutils.core import setup

setup(
    name="Pomerd Pests",
    py_modules=["pests"],
    entry_points={"console_scripts": ["pests=pests:main"]},
    version="0.2.6",
    description="Düşük bant genişliğine sahip DDoS aracı.",
    author="Pomerd",
    url="https://t.me/p0merdaga",
    keywords=["dos", "http", "pests"],
    license="MIT",
)
