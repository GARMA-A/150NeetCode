const std = @import("std");
const testing = std.testing;

pub fn Stack(comptime T: type) type {
    return struct {
        const Self = @This();
        const Node = struct { value: T, next: ?*Node };
        allocator: std.mem.Allocator,
        top: ?*Node,
        pub fn init(allocator: std.mem.Allocator) Self {
            std.log.info("\n--- init the stack ---\n", .{});
            return Self{ .allocator = allocator, .top = null };
        }
        pub fn deinit(self: *Self) void {
            std.log.info("\n--- deinit the stack ---\n", .{});
            while (self.pop()) |_| {}
        }
        pub fn push(self: *Self, value: T) !void {
            std.log.info("\n--- push {any} to the stack ---\n", .{value});
            const node = try self.allocator.create(Node);
            node.value = value;
            node.next = self.top;
            self.top = node;
        }
        pub fn pop(self: *Self) ?T {
            std.log.info("\n--- pop {any} from the stack ---\n", .{self.top});
            const node = self.top orelse return null;
            defer self.allocator.destroy(node);
            self.top = node.next;
            return node.value;
        }
        pub fn peek(self: *Self) ?T {
            std.log.info("\n--- peek {any} the stack ---\n", .{self.top});
            if (self.top) |node| {
                return node.value;
            }
            return null;
        }
        pub fn print(self: *Self) void {
            std.log.info("\n--- print the stack ---\n", .{});
            var curr = self.top;
            while (curr) |node| : (curr = node.next) {
                std.debug.print("{d} , ", .{node.value});
            }
        }
    };
}

test "stack impl testing" {
    var my_stack = Stack(i32).init(testing.allocator);
    defer my_stack.deinit();
    try my_stack.push(42);
    try testing.expect(my_stack.peek() == 42);
    try my_stack.push(100);
    try testing.expect(my_stack.peek() == 100);
    try testing.expect(my_stack.pop() == 100);
    try testing.expectEqual(42, my_stack.pop());
}

test "skip test case" {
    return error.SkipZigTest;
    // any logic here will be skipped
}
