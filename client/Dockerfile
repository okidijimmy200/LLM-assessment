FROM node:20-alpine3.19

ENV TZ=Africa/Kampala

LABEL version="1.0"
LABEL descriptionn="Development image for Client"

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 8080

CMD  ["npm", "run", "dev"]