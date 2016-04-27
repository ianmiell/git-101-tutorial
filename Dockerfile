FROM ubuntu:14.04
# Step 2 done
RUN apt-get update && apt-get install -y lsb-release && mkdir -p myproject && touch /root/.bash_history
# Step 3 done
WORKDIR /myproject
# Step 4 done
RUN a command && echo 'a command' >> /root/.bash_history
# Step n done
CMD /bin/bash