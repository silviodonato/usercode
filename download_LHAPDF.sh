#See https://lhapdf.hepforge.org/

wget https://lhapdf.hepforge.org/downloads/?f=LHAPDF-6.2.3.tar.gz -O LHAPDF-6.2.3.tar.gz
tar xzf  LHAPDF-6.2.3.tar.gz
cd LHAPDF-6.2.3
./configure --prefix=/home/sdonato/CMS/LHAPDF
make
make install
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/sdonato/CMS/LHAPDF/lib
wget http://lhapdfsets.web.cern.ch/lhapdfsets/current/NNPDF23_lo_as_0130_qed.tar.gz -O- | tar xz -C /home/sdonato/CMS/LHAPDF/share/LHAPDF

