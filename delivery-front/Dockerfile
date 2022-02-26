FROM node:16.13.2-alpine

WORKDIR /delivery-frontend
ENV PATH /delivery-frontend/node_modules/.bin:$PATH

COPY package.json ./
RUN npm i --silent
RUN npm install
