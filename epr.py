puckage com.accp.jap.bean;

import com.sun.javafx.beans.IDProperty;
import lombok.Data;
import org.springframework.stereotype.Component;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;

/**
 * @项目名: jap
 * @包名: com.accp.jap.bean
 * @作者: Administrator:趙赴起
 * @创建时间: 2020-5-11 19:34
 * @描述:
 */
@Data
@Entity
@Table(name = "addres")
public class Addres {
    @Id
    @GeneratedValue
    private Integer id;
    private String name;
}
epy.com
