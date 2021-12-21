sudo docker build ./ -t bot
sudo docker run -e TELEBOT_TOKEN=$TELEBOT_TOKEN bot
