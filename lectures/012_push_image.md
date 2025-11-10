## Push Image
เป็นการอัพโหลด image ขึ้นไปไว้บน docker hub เพื่อให้คนอื่นสามารถดึง image ไปใช้ได้

โดยมีขั้นตอนที่จะต้องทำดังนี้
1. สร้าง repository บน docker hub
2. build image หรือ นำ image มาใช้งาน
3. กำหนด tag image ให้กับ repository
4. push image ขึ้น docker hub

### Tag Image
เป็นการระบุว่า ใครคือเจ้าของ image (username) เก็บไว้ใน repository ใดและมีเวอร์ชันอะไรบ้าง

### โครงสร้างคำสั่ง
    docker tag <local-image:tag> <dockerhub-username/repository:tag>
**ตัวอย่าง**
    
    docker tag my-python-container:0.0.1 <dockerhub-username>/python-hello-world:0.0.1

*tag มีต่า latest เป็นค่าเริ่มต้น*

### โครงสร้างคำสั่งนำ image ขึ้น docker hub
    docker push <username>/python-hello-world