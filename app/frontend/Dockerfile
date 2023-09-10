FROM node:16

WORKDIR /home/frontend

COPY package*.json ./

COPY . .

RUN npm install
# RUN npm run build

CMD ["npm", "run", "dev"]
