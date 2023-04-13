import React from "react";
import { NavLink } from "react-router-dom";
import s from './ListPerfomance.module.scss'
import { PerfomanceCard } from "../../Cards/PerfomanceCard/PerfomanceCard";

export const ListPerfomance = () => {
    return (
        <div className={s.wrapper}>
            <div className={s.search}>
                <div>
                    <input type="text" />
                </div>
                <div className={s.input}>Поиск</div>
            </div>
            <div className={s.categories}>
                <NavLink to='/'>Все услуги</NavLink>
                <span>Название категории</span>
            </div>
            <div className={s.cards}>
                <PerfomanceCard />
                <PerfomanceCard />
                <PerfomanceCard />
            </div>
        </div>
    )
}