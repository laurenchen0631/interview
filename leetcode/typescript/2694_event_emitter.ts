type Callback = (...args: any[]) => any;
type Subscription = {
    unsubscribe: () => void
}

class EventEmitter {
    subscriptions: Map<string, Callback[]> = new Map();

    subscribe(eventName: string, callback: Callback): Subscription {
        if (!this.subscriptions.has(eventName)) {
            this.subscriptions.set(eventName, []);
        }
        this.subscriptions.get(eventName)!.push(callback);

        return {
            unsubscribe: () => {
                this.subscriptions.set(
                    eventName,
                    this.subscriptions.get(eventName)!.filter(cb => cb !== callback)
                );
            }
        };
    }

    emit(eventName: string, args: any[] = []): any[] {
        if (!this.subscriptions.has(eventName)) {
            return [];
        }
        return this.subscriptions.get(eventName)!.map(cb => cb(...args));
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */