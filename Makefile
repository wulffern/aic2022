
pan:
	./d2pan

note:
	rm -rf deliv_notes
	mkdir deliv_notes
	mv pandoc/*.pdf deliv_notes

cpm:
	cp ../dic_2021/dic2021/media/${FILE} media/
