FROM debian
# Step 1 done
RUN apt-get update && apt-get install -y git lsb-release vim bsdmainutils man-db manpages && mkdir -p /myproject && touch /root/.bash_history
# Step 2 done
WORKDIR /myproject
# Step 3 done
RUN git config --global user.email "you@example.com" && git config --global user.name "Your Name" && echo 'git config --global user.email "you@example.com" && git config --global user.name "Your Name"' >> /root/.bash_history
# Step 4 done
RUN git init && echo 'git init' >> /root/.bash_history
# Step 5 done
RUN echo "#!/usr/bin/env python" > mycode.py && echo 'echo "#!/usr/bin/env python" > mycode.py' >> /root/.bash_history
# Step 6 done
RUN git add mycode.py && echo 'git add mycode.py' >> /root/.bash_history
# Step 7 done
RUN git commit -m 'mycode.py added' && echo "git commit -m 'mycode.py' added" >> /root/.bash_history
# Step 8 done
RUN echo "import string" >> mycode.py && echo 'echo "import string" >> mycode.py' >> /root/.bash_history
# Step 9 done
RUN git commit -am 'import added' && echo "git commit -am 'import added" >> /root/.bash_history
# Step 10 done
CMD /bin/bash
# Step 11 done
