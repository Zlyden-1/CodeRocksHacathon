import React from "react";
import s from './PersonalAccount.module.scss'
import { AiFillStar } from 'react-icons/ai'
import { SiGooglemaps } from 'react-icons/si'
import { OrderCard } from "../../Cards/OrderCard/OrderCard";

export const PersonalAccount = () => {
    return (
        <div className={s.wrapper}>
            <div className={s.wrapperinfo}>
                <div className={s.imgcontent}>
                </div>
                <div className={s.textcontent}>
                    <span class={s.nameuser}>Карла Августина <AiFillStar />4.5</span>
                    <div><SiGooglemaps />  Самара</div>
                    <span class={s.editabletext} contenteditable>Опишите себя</span>
                    <div style={{ marginTop: '10px' }}>Обладаю большим опытом работы в сфере обучения, как с детьми, так и со студентами разных уровней подготовки. Всегда стремлюсь найти индивидуальный подход к каждому ученику, учитывая его..</div>
                </div>
            </div>
            <div className={s.button}>Изменить фото</div>
            <div className={s.wrapperhead}>
                <div className={s.textcat}>
                    Активные заказы
                </div>
                <div className={s.button}>Создать заказ</div>
            </div>
            <div className={s.orders}>
                <OrderCard/>
                <OrderCard/>
                <OrderCard/>
            </div>
        </div>
    )
}