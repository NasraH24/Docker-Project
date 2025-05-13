
# Flask + Redis + Nginx (Docker Compose Project)

This project demonstrates a basic multi-container application setup using:

- **Flask** (Python web application)
- **Redis** (in-memory key-value store)
- **Nginx** (reverse proxy and load balancer)
- **Docker Compose** (for orchestration)

## How It Works

- The **Flask app** provides two routes:
  - `/` — Displays a welcome message
  - `/count` — Increments and displays a visit count stored in **Redis**
- **Redis** stores the visitor count.
- **Nginx** acts as a reverse proxy and balances incoming requests across multiple Flask instances.

## Starting the Application

To start the application, run:
```bash
docker-compose up --build
```

Then visit: [http://localhost:5002](http://localhost:5002)

- The `/` route displays a welcome message.
- The `/count` route increments and displays the visit count stored in **Redis**.

To stop and remove all running containers:
```bash
docker-compose down
```

## Future Improvements

- Add **health checks** to monitor the availability of services.
- Implement **logging and monitoring** with tools like **Prometheus** and **Grafana**.
- Configure **HTTPS termination** at the Nginx reverse proxy.
- Set up **automatic scaling** using **Docker Swarm** or **Kubernetes**.

## Screenshots

### Home Page (`/`)

<p align="center">
  <img src="images/home-page.png" alt="Home Page" width="600"/>
</p>

### Count Page (`/count`)

<p align="center">
  <img src="images/count-page.png" alt="Count Page" width="600"/>
</p>
