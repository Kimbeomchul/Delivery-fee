FROM node:16.13.2-alpine

WORKDIR /delivery-front
ENV PATH /delivery-front/node_modules/.bin:$PATH

COPY package.json ./
RUN npm i --silent
RUN npm install
