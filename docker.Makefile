pideck_0.2-4_armhf.deb :
	docker build -t pideck-dev .
	docker run -v $$(pwd):/root/src -w /root/src pideck-dev \
	bash -c "dpkg-buildpackage -aarmhf -uc -us -b && \
	         mv ../$@ ."
