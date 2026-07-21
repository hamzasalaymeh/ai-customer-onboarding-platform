# Frontend

React + TypeScript single-page app (built with Vite) for the customer
onboarding wizard and AI chat assistant.

## Setup

```bash
npm install
cp .env.example .env
```

## Run

```bash
npm run dev
```

App: http://localhost:5173 (proxies `/api` to the backend on port 8000)

## Build

```bash
npm run build
```

## Layout

```
src/
├── main.tsx            App entry point
├── App.tsx              Top-level layout/routing
├── api/                 Backend API client
├── components/          Reusable UI components
├── pages/                Route-level views
├── types/                Shared TypeScript types
└── styles/              Global styles
```
