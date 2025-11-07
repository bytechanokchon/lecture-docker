## Container

## คำสั่งจัดการ Container
### docker run (image-name)
    รัน container จาก image
    ถ้าครั้งแรกจะทำการ pull image ให้อัตโนมัติในกรณีไม่พบ image บนเครื่อง

### docker run -d (image-name)
    รัน container แบบ background
    -d (detached) ส่วนใหญ่จะใช้ในงาน production

### docker run -it (image-name)
    รันแบบ interactive พร้อม shell เข้าใช้งานภายใน container
    พิมพ์ exit เพื่อออกจาก shell

### docker run --name (container-name) (image-name)
    รัน container พร้อมกำหนดชื่อของ container

### docker ps
    แสดงรายการ container ที่กำลังทำงานอยู่

### docker ps -a
    แสดงรายการ container ทั้งหมด (ที่ไม่ทำงานด้วย)

### docker container prune
    ลบ container ที่หยุดทำงานแล้วออก

### docker start (container-id)
    สั่งให้ container เริ่มต้นทำงาน

### docker stop (container-id)
    หยุดการทำงานของ container

### docker restart (container-id)
    รีสตาร์ท container

### docker pause (container-id)
    หยุดการทำงานชั่วคราว

### docker unpause (container-id)
    เริ่มทำงานต่อ

### docker rm (container-id)
    ลบ container ที่หยุดทำงานแล้ว

### docker rm -f (container-id)
    บังคับหยุด container (แม้จะทำงานอยู่ก็ตาม)

### docker run --rm (container-id)
    รัน container ขึ้นมา และทำการลบทันทีเมื่อ container ถูกปิดใช้งาน